---
id: UNC@20.15.2@MMLCommand@RMV SBINRFKEY
type: MMLCommand
name: RMV SBINRFKEY（删除NRF密钥）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SBINRFKEY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP OAuth安全管理
status: active
---

# RMV SBINRFKEY（删除NRF密钥）

## 功能

该命令用于删除NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。当NRF更新私钥时，需要删除老的公钥，并配置新的私钥所对应的公钥。

## 注意事项

- 该命令执行后立即生效。

- 删除NRF密钥会导致业务中断。在新的公钥、私钥及token生效后，业务才能恢复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFID | NRF实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的NRF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBINRFKEY]] · NRF密钥（SBINRFKEY）

## 使用实例

若运营商想删除NRF实例bf33a517-7789-4637-b675-b3591b0d706b的公钥信息，可以用如下命令：

```
RMV SBINRFKEY: NRFID="bf33a517-7789-4637-b675-b3591b0d706b ";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SBINRFKEY.md`
