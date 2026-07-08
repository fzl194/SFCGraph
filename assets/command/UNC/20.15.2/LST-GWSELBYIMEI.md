---
id: UNC@20.15.2@MMLCommand@LST GWSELBYIMEI
type: MMLCommand
name: LST GWSELBYIMEI（查询基于IMEI选择GGSN/P-GW配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWSELBYIMEI
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
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 基于IMEI选择GGSN P-GW
status: active
---

# LST GWSELBYIMEI（查询基于IMEI选择GGSN/P-GW配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询基于IMEI选择GGSN/P-GW配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指示IMEI群组标识，<br>UNC<br>需要为这些类型终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELBYIMEI]] · 基于IMEI选择GGSN/P-GW配置（GWSELBYIMEI）

## 使用实例

查询IMEI群组标识为1的基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI: IMEIGPID=1;

```
%%LST GWSELBYIMEI:IMEIGPID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

查询所有基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI:;

```
%%LST GWSELBYIMEI:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GWSELBYIMEI.md`
