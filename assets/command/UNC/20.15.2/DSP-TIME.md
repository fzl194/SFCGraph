---
id: UNC@20.15.2@MMLCommand@DSP TIME
type: MMLCommand
name: DSP TIME（查询系统时间）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TIME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 时区夏令时管理
status: active
---

# DSP TIME（查询系统时间）

## 功能

本命令用于请求系统的当前时间。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [系统时间（TIME）](configobject/UNC/20.15.2/TIME.md)

## 使用实例

显示当前容器时间。时区为东8区，夏令时偏移量为10分钟，已进入夏令时内（DST为夏令时标志）：

```
%%DSP TIME:;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------ 
当前系统时间  =  2020-03-26 10:07:36+08:10 DST
(结果个数 = 1)  
---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询系统时间（DSP-TIME）_33844132.md`
