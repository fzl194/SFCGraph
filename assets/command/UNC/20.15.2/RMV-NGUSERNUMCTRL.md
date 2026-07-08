---
id: UNC@20.15.2@MMLCommand@RMV NGUSERNUMCTRL
type: MMLCommand
name: RMV NGUSERNUMCTRL（删除5G接入用户数控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGUSERNUMCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 5G接入用户数控制
status: active
---

# RMV NGUSERNUMCTRL（删除5G接入用户数控制参数）

## 功能

![](删除5G接入用户数控制参数（RMV NGUSERNUMCTRL）_10217221.assets/notice_3.0-zh-cn_2.png)

执行该命令，ROAMNUMUPLIMIT参数设置不合理，可能会影响外网用户的接入。

**适用NF：AMF**

该命令用于删除指定Serving PLMN的5G接入用户数控制参数。

## 注意事项

删除接入用户数相关控制参数，仅对新接入用户生效，已接入用户不受影响。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数表示需要限制接入漫游用户数的Serving PLMN。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>PLMNIDX已通过ADD NGSRVPLMN进行配置。 |

## 操作的配置对象

- [5G接入用户数控制参数（NGUSERNUMCTRL）](configobject/UNC/20.15.2/NGUSERNUMCTRL.md)

## 使用实例

索引为1的Serving PLMN不再需要做接入用户数控制，执行如下命令：

```
RMV NGUSERNUMCTRL:PLMNIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G接入用户数控制参数（RMV-NGUSERNUMCTRL）_10217221.md`
