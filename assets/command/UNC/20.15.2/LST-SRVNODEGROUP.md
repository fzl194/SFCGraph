---
id: UNC@20.15.2@MMLCommand@LST SRVNODEGROUP
type: MMLCommand
name: LST SRVNODEGROUP（查询服务节点组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVNODEGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于对接IP地址的虚拟APN映射管理
- 虚拟APN映射的服务节点组
status: active
---

# LST SRVNODEGROUP（查询服务节点组）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来查看指定服务节点组或者已配置所有服务节点组的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 服务节点组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务节点组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SRVNODEGROUP]] · 服务节点组（SRVNODEGROUP）

## 使用实例

- 查询指定服务节点组的信息：
  ```
  %%LST SRVNODEGROUP: GROUPNAME="huawei";%%
  RETCODE = 0  操作成功

  查询SRVNODEGROUP
  ----------------
  服务节点组名称  =  huawei
  (结果个数 = 1)

  ---    END
  ```
- 查询已配置所有服务节点组的配置信息：
  ```
  %%LST SRVNODEGROUP:;%%
  RETCODE = 0  操作成功

  查询SRVNODEGROUP
  ----------------
  服务节点组名称  

  huawei                  
  huawei1                 
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVNODEGROUP.md`
