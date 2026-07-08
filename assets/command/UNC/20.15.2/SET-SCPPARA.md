---
id: UNC@20.15.2@MMLCommand@SET SCPPARA
type: MMLCommand
name: SET SCPPARA（设置SCP参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCPPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- SCP信息管理
status: active
---

# SET SCPPARA（设置SCP参数）

## 功能

![](设置SCP参数（SET SCPPARA）_98868309.assets/notice_3.0-zh-cn_2.png)

在通过DSP SBILINKSET命令查询SCP链路存在的情况下，将DISCPOLICY设置为“LOCAL_ONLY”且未通过ADD PNFPROFILE配置SCP，或将DISCPOLICY设置为“REMOTE_ONLY”且没有满足条件的SCP注册到NRF上时，本端网元会因选不到SCP导致间接路由业务中断。

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于设置SCP参数。

## 注意事项

- 该命令执行后立即生效。

- 当本端网元未配置ScpDomain服务发现SCP时，使用SCP发布的NFProfile中的IP地址建链。
- 服务发现SCP时不在缓存中查找，参考缓存功能关闭的场景。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DISCPOLICY | SCPDOMAINSW | DISCPERIOD |
| --- | --- | --- |
| LOCAL_ONLY | ON | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DISCPOLICY | 服务发现策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCP服务发现策略。<br>数据来源：全网规划<br>取值范围：<br>- “LOCAL_FIRST（LOCAL_FIRST）”：本地优先，先从本地配置查找满足服务发现条件的网元，如没有命中服务发现条件则再去缓存查找（如果缓存功能关闭，则跳过此步），如仍无命中则再去NRF查找。<br>- “LOCAL_ONLY（LOCAL_ONLY）”：仅本地查找，只从本地配置查找。<br>- “REMOTE_ONLY（REMOTE_ONLY）”：仅远端查找，先在缓存查找（如果缓存功能关闭，则跳过此步），如没命中则再去NRF查找。<br>- “REMOTE_FIRST（REMOTE_FIRST）”：远端优先，先在缓存查找满足服务发现条件的网元（如果缓存功能关闭，则跳过此步），如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPPARA查询当前参数配置值。<br>配置原则：<br>本地和远端为互补或相互备份的关系，如果在某一策略下能在某一数据来源中找到满足要求的SCP，则此处不会在另一数据来源中再进行服务发现。 |
| SCPDOMAIN | SCPDOMAIN | 可选必选说明：可选参数<br>参数含义：该参数用于表示本端NF所属的SCPDOMAIN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPPARA查询当前参数配置值。<br>配置原则：无 |
| SCPDOMAINSW | SCPDOMAIN开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定从NRF服务发现SCP时，是否开启强制携带SCPDOMAIN的开关。如果开关设置为"ON"，表示从NRF服务发现SCP时需要强制携带SCPDOMAIN，即参数DISCPOLICY设置为“LOCAL_FIRST”，“REMOTE_ONLY”，“REMOTE_FIRST”时，会校验参数SCPDOMAIN不能为空。如果开关设置为“OFF”，表示不强制携带SCPDOMAIN，不会校验SCPDOMAIN是否为空，如果SCPDOMAIN非空，从NRF发现SCP时仍携带SCPDOMAIN。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPPARA查询当前参数配置值。<br>配置原则：无 |
| DISCPERIOD | 发现周期 (分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCP服务发现周期。本端NF按发现周期，周期性服务发现SCP。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~2880，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SCP参数（SCPPARA）](configobject/UNC/20.15.2/SCPPARA.md)

## 使用实例

将本端网元所属的SCPDOMAIN设置为"domain1"。

```
SET SCPPARA: SCPDOMAIN="domain1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SCP参数（SET-SCPPARA）_98868309.md`
