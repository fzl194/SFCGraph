---
id: UNC@20.15.2@MMLCommand@LST IMRFUNC
type: MMLCommand
name: LST IMRFUNC（查询用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMRFUNC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 信令采集
status: active
---

# LST IMRFUNC（查询用户消息统计功能配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询用户消息统计功能配置。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>默认值 ：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_USER”<br>后生效。<br>数据来源：全网规划<br>取值范围：5~15位数字<br>默认值 ：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMRFUNC]] · 用户消息统计功能配置（IMRFUNC）

## 使用实例

查询IMRFUNC参数设置：

LST IMRFUNC:;

```
%%LST IMRFUNC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 用户范围  IMSI前缀  接口类型

 所有用户  NULL      NULL
 指定用户  123000    S11接口 & S6a接口 & SGs接口 & Sv接口
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMRFUNC.md`
