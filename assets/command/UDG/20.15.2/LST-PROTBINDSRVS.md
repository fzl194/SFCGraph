---
id: UDG@20.15.2@MMLCommand@LST PROTBINDSRVS
type: MMLCommand
name: LST PROTBINDSRVS（查询业务统计协议绑定配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTBINDSRVS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务统计协议绑定
status: active
---

# LST PROTBINDSRVS（查询业务统计协议绑定配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看基于业务的性能统计组合中的Protocol和Protocol Group对象。

## 注意事项

该命令支持批量查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVSTATNAME | 业务统计名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTBINDSRVS]] · 业务统计协议绑定配置（PROTBINDSRVS）

## 使用实例

- 运营商希望查看基于业务的性能统计组合“stat1”所绑定的协议和协议组：
  ```
  LST PROTBINDSRVS:SRVSTATNAME="stat1";
  ```
  ```

  RETCODE = 0  操作成功。

  业务统计协议绑定信息
  --------------------
  业务统计名称    协议等级          协议组名称     协议名称  

  stat1           Protocol Group    definegroup    NULL      
  stat1           Protocol Group    p2p            NULL      
  stat1           Protocol          NULL           protdefine
  (结果个数 = 3)
  ---    END
  ```
- 运营商希望查询所有基于业务的性能统计配置所绑定的Protocol和Protocol Group对象：
  ```
  LST PROTBINDSRVS:;
  ```
  ```

  RETCODE = 0  操作成功。

  业务统计协议绑定信息
  --------------------
  业务统计名称    协议等级          协议组名称     协议名称   

  stat1           Protocol Group    definegroup    NULL       
  stat1           Protocol Group    p2p            NULL       
  stat1           Protocol          NULL           protdefine 
  stat2           Protocol          NULL           protdefine1
  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务统计协议绑定配置（LST-PROTBINDSRVS）_86527040.md`
