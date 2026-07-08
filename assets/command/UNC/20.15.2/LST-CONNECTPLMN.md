---
id: UNC@20.15.2@MMLCommand@LST CONNECTPLMN
type: MMLCommand
name: LST CONNECTPLMN（查询互联PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CONNECTPLMN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 互联PLMN管理
status: active
---

# LST CONNECTPLMN（查询互联PLMN）

## 功能

**适用网元：SGSN、MME**

此命令用于查看互联PLMN控制表，通过查看该表，可以看出某个互联PLMN是否允许接入并进行相应业务。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：待查询的互联PLMN的移动国家号码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：待查询的互联PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：待查询的除了MCC和MNC外的IMSI的字段。<br>取值范围：长度不超过10的十进制数字<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：待查询的与互联PLMN签订漫游协议的本局运营商标识。<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CONNECTPLMN]] · 互联PLMN（CONNECTPLMN）

## 使用实例

查询所有的互联PLMN：

LST CONNECTPLMN:;

```
%%LST CONNECTPLMN:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
            移动国家码  =  460
              移动网号  =  00
              匹配IMSI  =  1234
                国家码  =  860
            运营商标识  =  0
        是否允许SM业务  =  允许
            最大承载数  =  11
       是否允许SMS业务  =  允许
是否允许纠正短消息中心  =  不允许
    纠正后的短消息中心  =  NULL
       是否允许LCS业务  =  不允许
              协议类型  =  GTP
            运营商名称  =  noname
          专属互连PLMN  =  否
  是否允许紧急呼叫业务  =  允许
      紧急号码下发开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CONNECTPLMN.md`
