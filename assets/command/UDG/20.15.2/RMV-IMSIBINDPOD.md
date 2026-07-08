---
id: UDG@20.15.2@MMLCommand@RMV IMSIBINDPOD
type: MMLCommand
name: RMV IMSIBINDPOD（删除IMSI和Pod的绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IMSIBINDPOD
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- Imsi绑定Pod
status: active
---

# RMV IMSIBINDPOD（删除IMSI和Pod的绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用于删除IMSI和POD的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIBINDPOD]] · IMSI和Pod的绑定关系（IMSIBINDPOD）

## 使用实例

当不再需要IMSI为1234567890的用户在特定的POD上激活，进行如下设置：

```
RMV IMSIBINDPOD: IMSI="123456789";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IMSI和Pod的绑定关系（RMV-IMSIBINDPOD）_64015277.md`
