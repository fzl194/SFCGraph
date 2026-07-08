---
id: UNC@20.15.2@MMLCommand@LST SRVNODEIP
type: MMLCommand
name: LST SRVNODEIP（查询服务节点IP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVNODEIP
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
- 服务节点组的服务节点IP段
status: active
---

# LST SRVNODEIP（查询服务节点IP）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来查询SGSN/SGW/PCF服务节点组与服务节点IP的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 服务节点组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务节点组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>本参数通过ADD SRVNODEGROUP命令进行配置。 |
| IPSECTIONID | 服务节点IP地址段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务节点IP地址段的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [服务节点IP（SRVNODEIP）](configobject/UNC/20.15.2/SRVNODEIP.md)

## 使用实例

- 查询指定服务节点组与服务节点地址段的绑定关系：
  ```
  %%LST SRVNODEIP: GROUPNAME="huawei";%%
  RETCODE = 0  操作成功

  服务节点IP配置信息
  -----------------------
                服务节点组名称  =  huawei
          服务节点IP地址段编号  =  1
                        IP版本  =  IPV6
  服务节点IPV4地址段的起始地址  =  0.0.0.0
  服务节点IPV4地址段的结束地址  =  0.0.0.0
  服务节点IPV6地址段的起始地址  =  2001:DB8::1
  服务节点IPV6地址段的结束地址  =  2001:DB8::2
  (结果个数 = 1)
  ---    END
  ```
- 查询指定服务节点地址段与服务节点组的绑定关系：
  ```
  %%LST SRVNODEIP: IPSECTIONID=1;%%
  RETCODE = 0  操作成功。

  服务节点IP配置信息
  -----------------------
                服务节点组名称  =  huawei
          服务节点IP地址段编号  =  1
                        IP版本  =  IPV6
  服务节点IPV4地址段的起始地址  =  0.0.0.0
  服务节点IPV4地址段的结束地址  =  0.0.0.0
  服务节点IPV6地址段的起始地址  =  2001:DB8::1
  服务节点IPV6地址段的结束地址  =  2001:DB8::2
  (结果个数 = 1)
  ---    END
  ```
- 查询所有服务节点地址段和服务节点组的绑定关系：
  ```
  %%LST SRVNODEIP:;%%
  RETCODE = 0  操作成功。

  服务节点IP配置信息
  -----------------------
                服务节点组名称  =  huawei
          服务节点IP地址段编号  =  1
                        IP版本  =  IPV6
  服务节点IPV4地址段的起始地址  =  0.0.0.0
  服务节点IPV4地址段的结束地址  =  0.0.0.0
  服务节点IPV6地址段的起始地址  =  2001:DB8::1
  服务节点IPV6地址段的结束地址  =  2001:DB8::2
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务节点IP（LST-SRVNODEIP）_09651392.md`
