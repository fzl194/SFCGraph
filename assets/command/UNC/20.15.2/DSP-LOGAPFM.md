---
id: UNC@20.15.2@MMLCommand@DSP LOGAPFM
type: MMLCommand
name: DSP LOGAPFM（显示日志代理性能统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LOGAPFM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 日志管理调测
status: active
---

# DSP LOGAPFM（显示日志代理性能统计信息）

## 功能

该命令用于显示日志代理性能统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程ID | 可选必选说明：可选参数<br>参数含义：用来表示进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [日志代理性能统计信息（LOGAPFM）](configobject/UNC/20.15.2/LOGAPFM.md)

## 使用实例

显示日志代理性能统计信息：

```
DSP LOGAPFM:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID   日志数量    日志处理时间（毫秒）    消息数量    消息处理时间（毫秒）

1001     709         1349981                 65          49
1002     266         1027648                 27          4
1000     1350        1532615                 181         305
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示日志代理性能统计信息（DSP-LOGAPFM）_59103516.md`
