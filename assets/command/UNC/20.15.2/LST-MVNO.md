---
id: UNC@20.15.2@MMLCommand@LST MVNO
type: MMLCommand
name: LST MVNO（查询MVNO配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MVNO
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO配置表
status: active
---

# LST MVNO（查询MVNO配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询MVNO的配置。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：待查询MVNO的标识。<br>取值范围：1～64<br>默认值：无<br>说明：- 如果输入MVNOID参数，只是查询这个MVNO的配置。如果不输入MVNOID参数，查询所有的记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MVNO]] · MVNO配置信息（MVNO）

## 使用实例

查看所有的MVNO:

LST MVNO:;

```
%%LST MVNO:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  MVNO标识 = 1
运营商全称 = bbb
运营商简称 = b
  协议类型 = GTP
    时间戳 = 1623876055
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MVNO.md`
