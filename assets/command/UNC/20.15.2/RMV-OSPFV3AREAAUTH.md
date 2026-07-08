---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3AREAAUTH
type: MMLCommand
name: RMV OSPFV3AREAAUTH（删除OSPFv3区域认证配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3AREAAUTH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域认证配置
status: active
---

# RMV OSPFV3AREAAUTH（删除OSPFv3区域认证配置）

## 功能

该命令用于删除OSPFv3区域所使用的认证模式及验证口令。

![](删除OSPFv3区域认证配置（RMV OSPFV3AREAAUTH）_00600997.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果OSPFv3区域认证与邻居配置不同，可能会使此进程的OSPFv3邻接关系中断，造成业务影响。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPFv3区域认证，请确保和邻居认证配置相同，否则会导致邻接关系中断，影响业务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| AUTHENMODE | 认证模式 | 可选必选说明：必选参数<br>参数含义：认证模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- hmac-sha256：HMAC-SHA256密文验证模式。<br>默认值：无 |
| KEYID | 密文验证字标识符 | 可选必选说明：必选参数<br>参数含义：密文验证字标识符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3AREAAUTH]] · OSPFv3区域认证配置（OSPFV3AREAAUTH）

## 使用实例

删除OSPFv3区域0.0.0.0使用HMAC-SHA256认证：

```
RMV OSPFV3AREAAUTH:PROCID=1,AREAID="0.0.0.0",AUTHENMODE=hmac-sha256,KEYID=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPFV3AREAAUTH.md`
