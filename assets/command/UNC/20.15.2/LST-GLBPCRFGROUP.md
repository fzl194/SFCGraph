---
id: UNC@20.15.2@MMLCommand@LST GLBPCRFGROUP
type: MMLCommand
name: LST GLBPCRFGROUP（查询全局PCRF组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBPCRFGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 全局PCRF组
status: active
---

# LST GLBPCRFGROUP（查询全局PCRF组绑定关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来显示PCRF分组和指定的号段绑定关系，以及绑定优先级。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的IMSIMSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBPCRFGROUP]] · 全局PCRF组绑定关系（GLBPCRFGROUP）

## 使用实例

查询GLBPCRFGROUP信息：

```
LST GLBPCRFGROUP:;
```

```

RETCODE = 0  操作成功

全局PCRF组绑定关系
------------------
IMSI/MSISDN号段名称  =  ims
         PCRF组名称  =  pcr
             优先级  =  3026
               描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBPCRFGROUP.md`
