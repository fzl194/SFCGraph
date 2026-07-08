---
id: UNC@20.15.2@MMLCommand@DSP SDRPLYSYNCVER
type: MMLCommand
name: DSP SDRPLYSYNCVER（显示策略同步版本）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRPLYSYNCVER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPLYSYNCVER（显示策略同步版本）

## 功能

该命令用于显示策略key和最后同步的版本信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERID | 订阅者ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示订阅者ID，它可以通过命令<br>[**DSP SDRPLYSUBINFO**](显示所有策略订阅者信息（DSP SDRPLYSUBINFO）_71652974.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~2048。<br>默认值：无<br>配置原则：无 |
| POLICY | 策略 | 可选必选说明：必选参数<br>参数含义：该参数用于表示策略，它可以通过命令DSP SDRPLYSUBINFO获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRPLYSYNCVER]] · 策略同步版本（SDRPLYSYNCVER）

## 使用实例

查询策略key和最后同步的版本信息：

```
%%DSP SDRPLYSYNCVER: SUBSCRIBERID="12141222829448690613", POLICY="AppRoute";%%
RETCODE = 0  操作成功

结果如下
--------
策略Key        最新同步的版本信息

app-134-id-0   1654183778144807071  
app-1008-id-0  1654183778144333072
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRPLYSYNCVER.md`
