---
id: UNC@20.15.2@MMLCommand@LST IMEISVSEG
type: MMLCommand
name: LST IMEISVSEG（查询IMEISV号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMEISVSEG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMEISV号段
status: active
---

# LST IMEISVSEG（查询IMEISV号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询IMEISVSEG号段。

支持批量查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEISV号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEISVSEG]] · IMEISV号段（IMEISVSEG）

## 使用实例

查询IMEISV号段：

```
LST IMEISVSEG:;
```

```

RETCODE = 0  操作成功

IMEISV号段信息
--------------
    IMEISV号段名称  =  testsegmentname
    IMEISV号段类型  =  IMEI
IMEI号段起始字符串  =  22222222000000
IMEI号段结束字符串  =  22222222999999
  SV号段起始字符串  =  NULL
  SV号段结束字符串  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMEISV号段（LST-IMEISVSEG）_09897141.md`
