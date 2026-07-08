---
id: UNC@20.15.2@MMLCommand@LST LOCATIONREPORT
type: MMLCommand
name: LST LOCATIONREPORT（查询用户位置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCATIONREPORT
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- 用户位置信息上报开关
status: active
---

# LST LOCATIONREPORT（查询用户位置信息）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来查询用户实时位置上报信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCATIONREPORT]] · 用户位置信息（LOCATIONREPORT）

## 使用实例

显示用户位置配置信息上报的本地trigger配置：

```
%%LST LOCATIONREPORT:;%%
RETCODE = 0  操作成功。

结果如下
--------
        配置用户位置信息的trigger  =  使能
            配置路由区域的trigger  =  不使能
            配置跟踪区域的trigger  =  使能
      配置演进的全球小区的trigger  =  使能
        配置5G NR全球小区的trigger =  使能
  基于用户漫游属性控制ULI信息上报  =  NULL
  基于用户漫游属性控制RAI信息上报  =  NULL
  基于用户漫游属性控制TAI信息上报  =  NULL
 基于用户漫游属性控制ECGI信息上报  =  NULL
 基于用户漫游属性控制NCGI信息上报  =  NULL
   基于用户RAT类型控制ULI信息上报  =  NULL
   基于用户RAT类型控制RAI信息上报  =  NULL
   基于用户RAT类型控制TAI信息上报  =  NULL
  基于用户RAT类型控制ECGI信息上报  =  NULL
位置更新消息上报的迟滞控制时长(秒) =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户位置信息（LST-LOCATIONREPORT）_04484293.md`
