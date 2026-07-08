---
id: UNC@20.15.2@MMLCommand@DSP FABRICSUBHEALTHYLINK
type: MMLCommand
name: DSP FABRICSUBHEALTHYLINK（显示Fabric平面亚健康链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FABRICSUBHEALTHYLINK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 故障信息
status: active
---

# DSP FABRICSUBHEALTHYLINK（显示Fabric平面亚健康链路信息）

## 功能

该命令用于显示Fabric平面亚健康链路信息。

当系统上报“ALM-100339 Fabric链路出现亚健康”告警后，可使用该命令查询告警的详细信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCCELLID | 源端Cell ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定源端Cell ID，Cell ID可以通过<br>[**DSP MSPROCESS**](../../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| STARTTIME | 查询开始时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询开始时间，时间格式为"YYYY-MM-DD HH:MM:SS"。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>若不输入，则表示该参数不作为查询的限制条件。 |
| ENDTIME | 查询结束时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询结束时间，时间格式为"YYYY-MM-DD HH:MM:SS"。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>若不输入，则表示该参数不作为查询的限制条件。 |

## 操作的配置对象

- [Fabric平面亚健康链路信息（FABRICSUBHEALTHYLINK）](configobject/UNC/20.15.2/FABRICSUBHEALTHYLINK.md)

## 使用实例

显示Fabric平面亚健康链路信息：

```
%%DSP FABRICSUBHEALTHYLINK: SRCCELLID="vup-pod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
源端Cell ID        目的端Cell ID       源端TB  目的端TB  平面ID  告警上报时间         

vup-pod-0__103__0  vusn-pod-0__103__0  1045    1030      0       2023-06-21 10:34:54  
vup-pod-0__103__0  vusn-pod-0__103__0  1045    1030      1       2023-06-21 10:34:54  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Fabric平面亚健康链路信息（DSP-FABRICSUBHEALTHYLINK）_70609581.md`
