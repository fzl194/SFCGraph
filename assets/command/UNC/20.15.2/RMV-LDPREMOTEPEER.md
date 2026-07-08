---
id: UNC@20.15.2@MMLCommand@RMV LDPREMOTEPEER
type: MMLCommand
name: RMV LDPREMOTEPEER（删除LDP远端邻居）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LDPREMOTEPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP远端邻居管理
status: active
---

# RMV LDPREMOTEPEER（删除LDP远端邻居）

## 功能

该命令用于删除LDP远端邻居。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| REMOTEPEERNAME | 远端邻居名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端邻居名。配置LDP远端会话，需要指定远端邻居名和IP地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPREMOTEPEER]] · LDP远端邻居（LDPREMOTEPEER）

## 使用实例

删除LDP远端邻居：

```
RMV LDPREMOTEPEER:VRFNAME="_public_",REMOTEPEERNAME="r3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LDPREMOTEPEER.md`
