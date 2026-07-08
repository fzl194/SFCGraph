---
id: UNC@20.15.2@MMLCommand@DSP PREOCCUPYRES
type: MMLCommand
name: DSP PREOCCUPYRES（显示预占RU资源）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PREOCCUPYRES
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- RU资源
status: active
---

# DSP PREOCCUPYRES（显示预占RU资源）

## 功能

**适用NF：NCG**

该命令用于显示预占的RU资源。

## 注意事项

该命令需等待 [**ACT PREOCCUPYRES**](预占RU资源（ACT PREOCCUPYRES）_51174356.md) 命令执行成功30秒后执行。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PREOCCUPYRES]] · 预占RU资源（PREOCCUPYRES）

## 使用实例

显示预占的RU资源：

```
DSP PREOCCUPYRES:;
```

```
RETCODE = 0  操作成功。
结果如下:
---------
         RU类型  =  CG_SP_RU
       预占数量  =  2
RU所在的HOST ID  =  8BF6E523-1800-9391-B211-D21D0C3EDC2B;8BF6E523-1800-ECBF-B211-D21D26ABAE2C
   命令返回结果  =  成功
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PREOCCUPYRES.md`
