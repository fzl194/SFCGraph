---
id: UNC@20.15.2@MMLCommand@SET TIME
type: MMLCommand
name: SET TIME（设置系统时间）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TIME
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 时区夏令时管理
status: active
---

# SET TIME（设置系统时间）

## 功能

![](设置系统时间（SET TIME）_87176066.assets/notice_3.0-zh-cn_2.png)

修改系统时间可能会影响话务统计、告警、日志等数据记录中时间信息的准确性，导致计费时间错乱，证书、License以及用户数据过期，系统瘫痪等，请慎重使用。

本命令用于设置网元系统的当前时间。

## 注意事项

- 新设置的时间需要与网元系统当前时间间隔不超过30秒。
- 禁止在升级、打补丁、回退过程中、升级观察期内设置系统时间。
- 在集群时间同步正常的情况下，修改时间后会被同步成NFV_FusionStage的时间。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SYSTIME | 设置系统时间 | 可选必选说明：必选参数。<br>参数含义：用于指定当前网元系统时间。<br>取值格式：YYYY/MM/DD HH:MM:SS<br>取值范围：<br>- YYYY（年份）：1990~2037<br>- MM（月份）：1~12<br>- DD（日期）：1~31<br>- HH（小时）：00~23<br>- MM（分钟）：00~59<br>- SS（秒）：00~59<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TIME]] · 系统时间（TIME）

## 使用实例

1. 系统时间设置成功后结果如下：

```
%%SET TIME：SYSTIME=2021&03&01&15&56&10;%% 
RETCODE = 0  操作成功  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置系统时间（SET-TIME）_87176066.md`
