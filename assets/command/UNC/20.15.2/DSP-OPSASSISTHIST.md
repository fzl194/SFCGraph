---
id: UNC@20.15.2@MMLCommand@DSP OPSASSISTHIST
type: MMLCommand
name: DSP OPSASSISTHIST（显示系统助手的历史信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OPSASSISTHIST
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 开放可编程系统
status: active
---

# DSP OPSASSISTHIST（显示系统助手的历史信息）

## 功能

该命令用于显示系统助手的历史信息（一个助手最多显示五条历史记录）。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OPSASSISTHIST]] · 系统助手的历史信息（OPSASSISTHIST）

## 使用实例

显示系统助手的历史信息：

```
DSP OPSASSISTHIST:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
助手ID    助手名称                     助手类型    默认助手标志位    触发类型    触发事件名称    触发时间                 运行开始时间            运行结束时间             执行结果（正常（0） 异常（1） 用户取消（2））

2         _get_all_env.py              脚本       TRUE             订阅事件     --             Nov 28 2017 17:42:03    Nov 28 2017 17:42:03    Nov 28 2017 17:42:06    0
3         autoscaling_autoconfig.py    脚本       TRUE             订阅事件     --             Nov 28 2017 17:43:57    Nov 28 2017 17:43:57    Nov 28 2017 17:44:13    0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OPSASSISTHIST.md`
