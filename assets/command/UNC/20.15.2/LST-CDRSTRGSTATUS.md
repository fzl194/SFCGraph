---
id: UNC@20.15.2@MMLCommand@LST CDRSTRGSTATUS
type: MMLCommand
name: LST CDRSTRGSTATUS（查询话单缓存目录状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRSTRGSTATUS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费缓存
- 缓存目录
status: active
---

# LST CDRSTRGSTATUS（查询话单缓存目录状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看话单缓存目录状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRSTRGSTATUS]] · 话单缓存目录状态（CDRSTRGSTATUS）

## 使用实例

查看PODNAME为uncpod-011-30-0-217下的话单缓存目录状态信息：

```
LST CDRSTRGSTATUS:PODNAME="uncpod-011-30-0-217";
```

```

RETCODE = 0  操作成功

话单缓存目录状态
----------------
     POD名称  =  uncpod-011-30-0-217
话单缓存目录  =  /charge1
    目录状态  =  锁定
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单缓存目录状态（LST-CDRSTRGSTATUS）_09897007.md`
