---
id: UNC@20.15.2@MMLCommand@LST NRFIMSIRT
type: MMLCommand
name: LST NRFIMSIRT（查询IMSI号段路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFIMSIRT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- IMSI号段路由管理
status: active
---

# LST NRFIMSIRT（查询IMSI号段路由）

## 功能

![](查询IMSI号段路由（LST NRFIMSIRT）_09653131.assets/notice_3.0-zh-cn_2.png)

该命令可能返回报文数据量较大，执行会影响系统性能，可通过增加查询参数减少返回结果报文。

**适用NF：NRF**

该命令用于查询已配置的IMSI号段路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持IMSI号段路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为AUSF、PCF、UDM、CHF、CUSTOM_OCS、SMSF的路由转发功能，其他NF类型为预留功能。 |
| SEGSTART | 号段起始字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMSI号段配置的号段起始字符串。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMSI号段配置的号段结束字符串。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF实例组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于IMSI号段寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFIMSIRT]] · IMSI号段路由（NRFIMSIRT）

## 使用实例

查询指定NF类型的路由信息。例如，在H-NRF上，查询NF类型为PCF的IMSI号段及该NF归属的L-NRF实例组名称。执行：

```
%%LST NRFIMSIRT:NFTYPE=PCF;%%
RETCODE = 0  操作成功

结果如下
------------------------           
            NF类型 = PCF   
      号段起始字符 = 125126000000000 
      号段结束字符 = 225226999999999 
 归属NRF实例组名称 = L-NRF1  

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI号段路由（LST-NRFIMSIRT）_09653131.md`
