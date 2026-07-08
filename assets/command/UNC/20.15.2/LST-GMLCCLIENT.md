---
id: UNC@20.15.2@MMLCommand@LST GMLCCLIENT
type: MMLCommand
name: LST GMLCCLIENT（查询GMLC和LCS Client对照关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMLCCLIENT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC和LCS Client对照表
status: active
---

# LST GMLCCLIENT（查询GMLC和LCS Client对照关系）

## 功能

**适用网元：SGSN**

此命令用于查询GMLC和LCS CLIENT对照表中的GMLC和LCS CLIENT的对照关系。不输入参数时将显示本SGSN下配置的所有GMLC和LCS CLIENT的对照关系。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTNUM | LCS客户端号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LCS Client Number，是LCS客户端的E.164地址。<br>取值范围：1～16位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCCLIENT]] · GMLC和LCS Client对照关系（GMLCCLIENT）

## 使用实例

列出SGSN中所有存在的GMLC和LCS CLIENT的对照关系:

LST GMLCCLIENT:;

```
%%LST GMLCCLIENT:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
LCS客户端号码  =  861380123456789
     GMLC号码  =  861390123456789
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GMLCCLIENT.md`
