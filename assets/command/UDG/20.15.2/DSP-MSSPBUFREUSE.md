---
id: UDG@20.15.2@MMLCommand@DSP MSSPBUFREUSE
type: MMLCommand
name: DSP MSSPBUFREUSE（显示PBUF重用信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSPBUFREUSE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSPBUFREUSE（显示PBUF重用信息）

## 功能

该命令用于显示MSS的PBUF重用信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSPBUFREUSE]] · PBUF重用信息（MSSPBUFREUSE）

## 使用实例

显示微服务类型为104的微服务实例csdb-pod-0172-16-0-247__103__0上重用的PBUF信息：

```
%%DSP MSSPBUFREUSE: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-0-247__103__0";%%
RETCODE = 0  操作成功

结果如下:
---------
内存池名称   进程号  缓存数目  缓存索引  

PAE          0       0         -         
PAE          1       0         -         
PAE          2       0         -         
PAE          3       0         -         
PAE          254     0         -         
paeFmeaInfo  0       0         -         
paeFmeaInfo  1       0         -         
paeFmeaInfo  2       0         -         
paeFmeaInfo  3       0         -         
paeFmeaInfo  254     0         -         
(结果个数 = 10)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSPBUFREUSE.md`
