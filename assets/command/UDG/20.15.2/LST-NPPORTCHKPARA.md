---
id: UDG@20.15.2@MMLCommand@LST NPPORTCHKPARA
type: MMLCommand
name: LST NPPORTCHKPARA（查询NP端口检测的参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPPORTCHKPARA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP端口检测参数
status: active
---

# LST NPPORTCHKPARA（查询NP端口检测的参数）

## 功能

该命令用来查询NP端口检测的参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPPORTCHKPARA]] · NP端口检测的参数（NPPORTCHKPARA）

## 使用实例

查询NP端口检测的参数：

```
LST NPPORTCHKPARA:;
RETCODE = 0  操作成功

结果如下
--------
内联口带宽利用率告警上报阈值（%）  =  95
内联口带宽利用率告警恢复阈值（%）  =  90
外联口带宽利用率告警上报阈值（%）  =  90
外联口带宽利用率告警恢复阈值（%）  =  80
             NP间端口故障自愈开关  =  使能
       NP间端口故障时长阈值（秒）  =  3
                 TB出端口检测开关  =  使能
   TB出端口无效的时长阈值（毫秒）  =  2000
       检测TB出端口刷新的周期倍数  =  15
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NPPORTCHKPARA.md`
