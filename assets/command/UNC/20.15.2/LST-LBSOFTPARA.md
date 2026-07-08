---
id: UNC@20.15.2@MMLCommand@LST LBSOFTPARA
type: MMLCommand
name: LST LBSOFTPARA（查询CSLB软件调试参数表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LBSOFTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 公共调测
- 软件参数管理
status: active
---

# LST LBSOFTPARA（查询CSLB软件调试参数表）

## 功能

该命令用于查询CSLB系统软件参数信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数标识 | 可选必选说明：可选参数<br>参数含义：软件参数ID<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LBSOFTPARA]] · CSLB软件调试参数表（LBSOFTPARA）

## 使用实例

查询CSLB软件调试参数表中参数标识为1023的参数值:

LST LBSOFTPARA: PARAID=1023;

```
%%LST LBSOFTPARA: PARAID=1023;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
参数标识  =  1023
  参数值  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LBSOFTPARA.md`
