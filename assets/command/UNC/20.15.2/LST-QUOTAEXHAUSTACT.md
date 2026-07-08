---
id: UNC@20.15.2@MMLCommand@LST QUOTAEXHAUSTACT
type: MMLCommand
name: LST QUOTAEXHAUSTACT（查询配额耗尽后的动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QUOTAEXHAUSTACT
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
- 配额耗尽处理动作
status: active
---

# LST QUOTAEXHAUSTACT（查询配额耗尽后的动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询配额耗尽后的动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [配额耗尽后的动作（QUOTAEXHAUSTACT）](configobject/UNC/20.15.2/QUOTAEXHAUSTACT.md)

## 使用实例

查询融合计费模板名为global的在线RG配额耗尽后动作为阻塞业务：

```
%%LST QUOTAEXHAUSTACT: CCTMPLTNAME="global";%%
RETCODE = 0  操作成功

结果如下
--------
    融合计费模板名称  =  global
在线RG配额耗尽后动作  =  阻塞业务，使业务不能继续进行
      重定向IPv4地址  =  0.0.0.0
      重定向IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询配额耗尽后的动作（LST-QUOTAEXHAUSTACT）_41849755.md`
