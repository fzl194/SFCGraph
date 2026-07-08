---
id: UDG@20.15.2@MMLCommand@LST ADCPARA
type: MMLCommand
name: LST ADCPARA（查询ADC参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ADCPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- ADC
- ADC参数
status: active
---

# LST ADCPARA（查询ADC参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询ADC参数。当运营商希望查询ADC下的流过滤器信息以及ADC的信息上报功能是否开启时，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器/流过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置应用对应的流过滤器或流过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ADCPARA]] · ADC参数（ADCPARA）

## 使用实例

假设运营商要查询指定ADC应用下的流信息上报开关信息，指定流过滤器名称为testflowfiltername：

```
LST ADCPARA:FLOWFILTERNAME="testflowfiltername";
```

```

RETCODE = 0  操作成功。

ADC参数信息
-----------
 流过滤器/流过滤器组名称  =  testflowfiltername
          流信息上报标识  =  不使能
应用级上报迟滞时间（秒）  =  0
          关键流检测开关  =  使能
         关键流时长（秒） =  5
关键流速率（千比特每秒）  =  50
              重定向名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ADCPARA.md`
