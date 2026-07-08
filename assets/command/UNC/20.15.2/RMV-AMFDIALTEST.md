---
id: UNC@20.15.2@MMLCommand@RMV AMFDIALTEST
type: MMLCommand
name: RMV AMFDIALTEST（删除AMF拨测用户配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFDIALTEST
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 灰度升级
- 拨测管理
status: active
---

# RMV AMFDIALTEST（删除AMF拨测用户配置）

## 功能

**适用NF：MME、AMF**

该命令用于删除一组拨测用户的配置。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 本命令的起始IMSI必须和LST AMFDIALTEST命令查询到的起始IMSI一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEGINIMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。不同记录的起始IMSI不能相同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF拨测用户配置（AMFDIALTEST）](configobject/UNC/20.15.2/AMFDIALTEST.md)

## 使用实例

删除一条拨测用户配置，起始IMSI为460001111111111，执行如下命令：

```
RMV AMFDIALTEST: BEGINIMSI="460001111111111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF拨测用户配置（RMV-AMFDIALTEST）_70382365.md`
