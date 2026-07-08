---
id: UDG@20.15.2@MMLCommand@LST SFERESALMTHD
type: MMLCommand
name: LST SFERESALMTHD（查询VNRS内部资源不足告警的阈值参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFERESALMTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- VNRS内部资源不足告警的阈值参数
status: active
---

# LST SFERESALMTHD（查询VNRS内部资源不足告警的阈值参数）

## 功能

该命令用来查询ALM-231612426 VNRS内部资源不足告警的阈值参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ALM-231612426 VNRS内部资源不足告警的资源类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4RecmpNode：IPv4分片重排节点。<br>- IPv4ReasmNode：IPv4分片重组节点。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFERESALMTHD]] · VNRS内部资源不足告警的阈值参数（SFERESALMTHD）

## 使用实例

查询IPv4分片重排节点资源不足导致的ALM-231612426 VNRS内部资源不足告警的阈值参数：

```
LST SFERESALMTHD: RESTYPE=IPv4RecmpNode:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
触发阈值（%）  =  90
恢复阈值（%）  =  80
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SFERESALMTHD.md`
