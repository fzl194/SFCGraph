---
id: UNC@20.15.2@MMLCommand@LST GWSELBYCC
type: MMLCommand
name: LST GWSELBYCC（查询基于CC选择GGSN/P-GW）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWSELBYCC
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
- GGSN_P-GW选择
status: active
---

# LST GWSELBYCC（查询基于CC选择GGSN/P-GW）

## 功能

**适用网元：SGSN、MME**

该命令用于查询基于CC选择GGSN/P-GW配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无 |
| SUBCC | 签约CC值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约CC值。<br>数据来源：全网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GWSELBYCC]] · 基于CC选择GGSN/P-GW（GWSELBYCC）

## 使用实例

查询所有基于IMEI选择P-GW/GGSN配置：

LST GWSELBYCC:;

```
%%LST GWSELBYCC:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
   APNNI  =  HUAWEI.COM
签约CC值  =  0x1234
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GWSELBYCC.md`
