---
id: UNC@20.15.2@MMLCommand@DSP PAENODE
type: MMLCommand
name: DSP PAENODE（显示PAE节点信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAENODE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP PAENODE（显示PAE节点信息）

## 功能

该命令用于显示PAE节点信息，查询到的结果均是Fabric类型的POD。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAENODE]] · PAE节点信息（PAENODE）

## 使用实例

显示PAE节点信息：

```
DSP PAENODE:;
```

```
RETCODE = 0  操作成功。
结果如下
--------
微服务类型   微服务实例号                                 工作角色    主备角色   服务地址                   资源ID        服务类型集合
104          vup-pod-1172-16-0-200__103__0                数据转发    None       vup-pod-1                  1039          CSLB 
104          vup-pod-0172-16-1-23__103__0                 数据转发    None       vup-pod-0                  1035          CSLB
129          sfm-pod-7b4dd4db47-fbbrt172-16-0-53__140__0  控制        备         sfm-pod-7b4dd4db47-fbbrt   4294967295    NULL
129          sfm-pod-7b4dd4db47-fbbrt172-16-0-53__140__0  控制        主         sfm-pod-7b4dd4db47-d6dnk   4294967295    NULL
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAENODE.md`
