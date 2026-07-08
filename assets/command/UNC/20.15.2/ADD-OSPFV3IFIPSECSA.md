---
id: UNC@20.15.2@MMLCommand@ADD OSPFV3IFIPSECSA
type: MMLCommand
name: ADD OSPFV3IFIPSECSA（创建OSPFv3 接口的安全联盟SA）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OSPFV3IFIPSECSA
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 8000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3接口安全联盟配置
status: active
---

# ADD OSPFV3IFIPSECSA（创建OSPFv3 接口的安全联盟SA）

## 功能

该命令用于创建OSPFv3 接口的安全联盟SA。

## 注意事项

该命令最大记录数为8000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST OSPFV3INTERFACE命令查看可用OSPFv3接口。 |
| SANAME | IPsec SA名称 | 可选必选说明：必选参数<br>参数含义：IPsec SA的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- IPsec SA必须已经存在。<br>- 不能直接修改，需要先删除再配置。<br>- 不能和认证同时配置。 |

## 操作的配置对象

- [创建OSPFv3 接口的安全联盟SA（OSPFV3IFIPSECSA）](configobject/UNC/20.15.2/OSPFV3IFIPSECSA.md)

## 使用实例

创建OSPFv3 接口的安全联盟SA：

```
ADD OSPFV3IFIPSECSA:IFNAME="Ethernet64/0/3",SANAME="sa1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/创建OSPFv3-接口的安全联盟SA（ADD-OSPFV3IFIPSECSA）_49802538.md`
