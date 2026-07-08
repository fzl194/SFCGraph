---
id: UNC@20.15.2@MMLCommand@LST IMSIGT
type: MMLCommand
name: LST IMSIGT（查询IMSI-GT对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIGT
command_category: 查询类
applicable_nf:
- SGSN
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- MAP应用协议
- IMSI GT转换信息
status: active
---

# LST IMSIGT（查询IMSI-GT对应关系）

## 功能

**适用网元：SGSN、SMSF**

该命令用于查看IMSI前缀与国家代码+网络接入号之间的对应关系。

## 注意事项

不输入查询条件的情况下，将所有记录都显示。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制数字<br>默认值：无<br>说明：IMSI前缀的查询匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIGT]] · IMSI-GT对应关系（IMSIGT）

## 使用实例

查询IMSI_GT转换表中的所有记录项:

LST IMSIGT:;

```
%%LST IMSIGT:;%%
RETCODE = 0  操作成功。

IMSI-GT转换表
-------------
 IMSI前缀    国家代码_网络接入号  移动网络名称

 1230319     8613919              noname      
 1230519     8613919              noname         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSIGT.md`
