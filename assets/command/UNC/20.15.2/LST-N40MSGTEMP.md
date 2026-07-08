---
id: UNC@20.15.2@MMLCommand@LST N40MSGTEMP
type: MMLCommand
name: LST N40MSGTEMP（查询N40消息属性模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40MSGTEMP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- N40消息属性模板
status: active
---

# LST N40MSGTEMP（查询N40消息属性模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询N40消息属性模板。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | N40消息属性模板名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N40消息字段模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40MSGTEMP]] · N40消息属性模板（N40MSGTEMP）

## 使用实例

查询名为“n40attr”的N40消息属性模板：

```
%%LST N40MSGTEMP: TEMPLATENAME="n40attr";%%
RETCODE = 0  操作成功

结果如下
--------
                 N40消息属性模板名  =  n40attr
        RANSecondaryRATUsageReport  =  携带该字段
                        NB扩展属性  =  携带该字段
         QFI容器中的DownLinkVolume  =  携带该字段
            HomeProvidedChargingID  =  携带该字段
               huaweiQBCIndication  =  不携带该字段
applicationserviceProviderIdentity  =  不携带该字段
            roamingChargingProfile  =  携带该字段
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N40MSGTEMP.md`
