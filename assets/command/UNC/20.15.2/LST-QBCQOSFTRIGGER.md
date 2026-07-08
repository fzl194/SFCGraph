---
id: UNC@20.15.2@MMLCommand@LST QBCQOSFTRIGGER
type: MMLCommand
name: LST QBCQOSFTRIGGER（查询QBC计费QoS Flow级的trigger参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QBCQOSFTRIGGER
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
- QBC计费QoS Flow级Trigger
status: active
---

# LST QBCQOSFTRIGGER（查询QBC计费QoS Flow级的trigger参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询QBC计费QoS Flow级的trigger参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [QBC计费QoS Flow级的trigger参数（QBCQOSFTRIGGER）](configobject/UNC/20.15.2/QBCQOSFTRIGGER.md)

## 使用实例

查询绑定名称为“test”的CCT融合计费模板的QBC计费QoS Flow级的trigger参数：

```
%%LST QBCQOSFTRIGGER: CCTMPLTNAME="test";%%
RETCODE = 0  操作成功

结果如下
--------
融合计费模板名称  =  test
         QoS更新  =  延迟上报
   QoS流时间阈值  =  延迟上报
   QoS流流量阈值  =  延迟上报
       QoS流结束  =  延迟上报
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QBC计费QoS-Flow级的trigger参数（LST-QBCQOSFTRIGGER）_09653168.md`
