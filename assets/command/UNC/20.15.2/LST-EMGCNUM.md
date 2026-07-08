---
id: UNC@20.15.2@MMLCommand@LST EMGCNUM
type: MMLCommand
name: LST EMGCNUM（查询紧急号码配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EMGCNUM
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- 紧急呼叫号码配置
status: active
---

# LST EMGCNUM（查询紧急号码配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询紧急号码的配置。

## 注意事项

如果没有输入参数，查询所有的记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询哪个移动国家码配置的紧急呼叫号码。<br>取值范围：3位的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EMGCNUM]] · 紧急号码信息表记录（EMGCNUM）

## 使用实例

查询所有的移动国家码下配置的紧急呼叫号码：

LST EMGCNUM:;

```
%%LST EMGCNUM:;%%
RETCODE = 0  操作成功。

紧急号码表
----------
 移动国家码  紧急服务分类  紧急呼叫号码

 123           报警          120         
 123           火警          119         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EMGCNUM.md`
