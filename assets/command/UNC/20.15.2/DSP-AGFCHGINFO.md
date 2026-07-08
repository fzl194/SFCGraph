---
id: UNC@20.15.2@MMLCommand@DSP AGFCHGINFO
type: MMLCommand
name: DSP AGFCHGINFO（显示AGF的计费上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AGFCHGINFO
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF的计费上下文信息
status: active
---

# DSP AGFCHGINFO（显示AGF的计费上下文信息）

## 功能

**适用NF：NCG**

该命令用于显示AGF的计费上下文信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGINGDATAREF | 计费数据标识 | 可选必选说明：必选参数<br>参数含义：该参数表示CTF与NCG间的计费数据标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>计费数据标识生成方式如下：<br>1）NCGSOFTPARA DWord4_Bit6为0，DWord28_BIt3为0时为：imsi（supi去掉imsi-前缀）+chargingId。<br>例：supi为imsi-460005896020654，chargingId为100000000，则计费数据标识为460005896020654100000000。<br>2）NCGSOFTPARA DWord4_Bit6为0，DWord28_BIt3为1时为：imsi（supi去掉imsi-前缀）+chargingId+PdusessionId。<br>例：supi为imsi-460005896020654，chargingId为100000000，PdusessionId为6，则计费数据标识为4600058960206541000000006。<br>3）NCGSOFTPARA DWord4_Bit6为1，DWord28_BIt3为0时为：chargingdataref。<br>请求消息的URL里chargingdata字段后的字符串即为chargingdataref。<br>4）NCGSOFTPARA DWord4_Bit6为1，DWord28_BIt3为1时为：chargingdataref+PdusessionId。<br>请求消息的URL里chargingdata字段后的字符串即为chargingdataref。<br>例：chargingdataref为338800000000111177555481138-00200022-000000001，PdusessionId为6，则计费数据标识为338800000000111177555481138-00200022-0000000016。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AGFCHGINFO]] · AGF的计费上下文信息（AGFCHGINFO）

## 使用实例

显示AGF的计费上下文信息：

```
DSP AGFCHGINFO: CHARGINGDATAREF="4600250000100011048620";
RETCODE = 0  操作成功
结果如下
--------
计费数据标识  =  4600250000100011048620
    计费信息  =  {
	"FailOverValue": "NULL",
	"FailureHandlingValue": "NULL",
	"InvocationTimeStamp": "2019-12-07T05:42:26Z",
	"LastUpdateTime": "2022-01-14T07:00:07Z",
	"LastOcsFaultTime": "1970-01-01T00:00:00Z",
	"NfInstance": "ocs_instance_gb",
	"UserLocationType": "LOCALUSER",
	"LastDiscCustomTime": "1970-01-01T00:00:00Z",
	"CdrLocation": "0"
}
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AGFCHGINFO.md`
