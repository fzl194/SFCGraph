---
id: UNC@20.15.2@MMLCommand@LST USRBLACKLST
type: MMLCommand
name: LST USRBLACKLST（查询用户黑名单限制列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRBLACKLST
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 黑名单接入限制
status: active
---

# LST USRBLACKLST（查询用户黑名单限制列表）

## 功能

![](查询用户黑名单限制列表（LST USRBLACKLST）_65074554.assets/notice_3.0-zh-cn_2.png)

如果黑名单限制列表记录过多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

**适用NF：SGSN、MME、AMF**

该命令用于查询黑名单限制的用户列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定限制用户黑名单接入的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRBLACKLST]] · 用户黑名单限制列表（USRBLACKLST）

## 使用实例

查询系统中黑名单限制的用户列表，执行如下命令：

```
%%LST USRBLACKLST:;%%
RETCODE = 0  操作成功

结果如下
--------
            IMSI  =  123456789012345
        限制模式  =  N2模式&S1模式&Iu模式&Gb模式
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户黑名单限制列表（LST-USRBLACKLST）_65074554.md`
