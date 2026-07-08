---
id: UNC@20.15.2@MMLCommand@DSP DYNAMICOCS
type: MMLCommand
name: DSP DYNAMICOCS（查询动态OCS）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DYNAMICOCS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- 动态OCS
status: active
---

# DSP DYNAMICOCS（查询动态OCS）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询动态OCS主机列表项。

DRA部署场景下，DRA进行OCS寻址，如果寻址到的OCS主机名并未在网关本地配置，则网关会将寻址结果存至动态OCS主机列表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSHOSTNAME | OCS主机名称 | 可选必选说明：可选参数<br>参数含义：主机的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [动态OCS（DYNAMICOCS）](configobject/UNC/20.15.2/DYNAMICOCS.md)

## 使用实例

- 查询指定主机名称的动态OCS信息：
  ```
  DSP DYNAMICOCS:OCSHOSTNAME="ocs-host-name";
  ```
  ```

  Dynamic OCS Information
  -------------------------
  OCS Host Name  =  ocs-host-name
     Realm Name  =  realm
  (Number of results = 1)
  ---    END
  ```
- 查询所有动态OCS信息：
  ```
  DSP DYNAMICOCS:;
  ```
  ```

  Dynamic OCS Information
  -------------------------
  OCS Host Name    Realm Name
  ocs-host-name    realm    
  ocs-name         realm    
  (Number of results = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询动态OCS（DSP-DYNAMICOCS）_09896973.md`
