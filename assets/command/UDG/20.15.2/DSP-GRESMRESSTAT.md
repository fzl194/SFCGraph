---
id: UDG@20.15.2@MMLCommand@DSP GRESMRESSTAT
type: MMLCommand
name: DSP GRESMRESSTAT（显示消费者申请资源的统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GRESMRESSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Gresm调测
status: active
---

# DSP GRESMRESSTAT（显示消费者申请资源的统计信息）

## 功能

该命令用于显示消费者申请资源的统计信息。APP向GRESM申请资源时，GRESM会记录申请的数量。通过用GRESM提供的命令DSP GRESMRESSTAT可以获取GRESM记录的数量，从而可以看出APP和GRESM资源数量是否一致。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [消费者申请资源的统计信息（GRESMRESSTAT）](configobject/UDG/20.15.2/GRESMRESSTAT.md)

## 使用实例

显示消费者申请资源的统计信息：

```
DSP GRESMRESSTAT:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
用户的PID     资源类型    正常使用资源的数量    错误一次的资源数量    错误两次的资源数量

0x210006      直连ID      0                     0                     0
0x220004      直连ID      22                    0                     0
0x6F0005      直连ID      22                    0                     0
0x700007      直连ID      0                     0                     0
0x790015      标签        0                     0                     0
0x790015      块标签      0                     0                     0
0xA60022      直连ID      0                     0                     0
0x1DA0003     直连ID      0                     0                     0
0x1DD000C     直连ID      60                    0                     0
0x2DE0001     直连ID      0                     0                     0
(结果个数 = 10)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示消费者申请资源的统计信息（DSP-GRESMRESSTAT）_00841389.md`
