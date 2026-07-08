---
id: UNC@20.15.2@MMLCommand@LST HSFNTIME
type: MMLCommand
name: LST HSFNTIME（查询H-SFN参考时间）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSFNTIME
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- H-SFN参考时间配置
status: active
---

# LST HSFNTIME（查询H-SFN参考时间）

## 功能

**适用网元：MME、AMF**

此命令用于查询当前配置的H-SFN=0的参考时间。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMETYPE | 时间类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置MME/AMF使用何种计时方式与eNodeB/NG-RAN对齐H-SFN=0的参考时间。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- GPS(GPS)<br>- UTC(UTC)<br>系统初始设置值：UTC(UTC)。<br>配置原则：MME/AMF支持UTC，GPS两种时间作为参考时间，使用时只能使用其中一种，使用何种方式需与eNodeB/NG-RAN侧协商一致 |
| GPSBEGIN | 使用GPS起始时间 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置MME/AMF是否使用GPS起始时间（1980年1月6日00:00:00）作为与eNodeB/NG-RAN对齐H-SFN=0的参考时间。<br>前提条件：该参数在<br>“时间类型”<br>参数配置为<br>“GPS”<br>后生效。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NO（否）。<br>- YES（是）。<br>系统初始设置值：NO（否）。 |
| DATE | H-SFN参考日期 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置H-SFN=0的具体日期，参数格式为“YYYY&MM&DD”，其中，“YYYY”代表年，“MM”代表月，“DD”代表日。<br>前提条件：<br>- 该参数在“使用GPS起始时间”参数配置为“否”后生效。<br>- 该参数在“时间类型”参数配置为“UTC”后生效。<br>数据来源：全网规划<br>取值范围：日期类型，输入格式是YYYY/MM/DD。（<br>日期限定只允许配置1990年1月1日至2037年12月31日<br>）<br>系统初始设置值：2010/01/01<br>配置原则：设置的日期为已经过去的某一日期，不能配置未来的日期。 |
| TIME | H-SFN参考时间 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置H-SFN=0的具体时间，输入格式为“HH:MM:SS”，“HH”代表时，“MM”代表分，“SS”代表秒。<br>前提条件：<br>- 该参数在“使用GPS起始时间”参数配置为“否”后生效。<br>- 该参数在“时间类型”参数配置为“UTC”后生效。<br>数据来源：全网规划<br>取值范围：时间类型，输入格式是HH:MM:SS。<br>系统初始设置值：00：00：00 |
| GPSLEAPSEC | 当前时间与参考时间闰秒差 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置当前时间与参考时间闰秒差。<br>前提条件：该参数在<br>“使用GPS起始时间”<br>参数设置后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>系统初始设置值：0。<br>配置原则：如果选择使用GPS起始时间（1980年1月6日00:00:00）作为H-SFN=0的参考时间，本参数设置值=最新公布的闰秒数-19（19为1980年1月1日公布的闰秒数）。如果设置了其他时间作为H-SFN=0的参考时间，本参数设置值=最新公布的闰秒数-设置的参考时间之前最近一次公布的闰秒数。闰秒数请到IERS官方网站查询：http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSFNTIME]] · H-SFN参考时间（HSFNTIME）

## 使用实例

查询H-SFN参考时间配置。

LST HSFNTIME:;

```
%%LST HSFNTIME:;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
                 时间类型  =  使用GPS时间作为H-SFN=0的参考时间
          使用GPS起始时间  =  否
            H-SFN参考日期  =  2000-01-01
            H-SFN参考时间  =  00:00:00
 当前时间与参考时间闰秒差  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HSFNTIME.md`
