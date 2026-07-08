---
id: UNC@20.15.2@MMLCommand@LST PERFNSE
type: MMLCommand
name: LST PERFNSE（查询NSE标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFNSE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# LST PERFNSE（查询NSE标识）

## 功能

**适用网元：SGSN**

该命令用于查询并显示所有的NSE标识。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNSE]] · NSE标识（PERFNSE）

## 使用实例

查询NSE列表中所有记录：

LST PERFNSE:;

```
%%LST PERFNSE:;%%
RETCODE = 0  执行成功。

NSE标识
-------
NSE标识

110
111
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFNSE.md`
