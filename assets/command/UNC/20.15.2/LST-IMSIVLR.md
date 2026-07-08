---
id: UNC@20.15.2@MMLCommand@LST IMSIVLR
type: MMLCommand
name: LST IMSIVLR（查询IMSI与VLR对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIVLR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- IMSI与VLR对应关系
status: active
---

# LST IMSIVLR（查询IMSI与VLR对应关系）

## 功能

**适用网元：MME**

该命令用于查询IMSI与MSC/VLR对应关系。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |
| VN | VLR号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端MSC/VLR提供的VLR号。<br>数据来源：全网规划<br>取值范围：1~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IMSI与VLR对应关系（IMSIVLR）](configobject/UNC/20.15.2/IMSIVLR.md)

## 使用实例

1.查询所有IMSI与MSC/VLR对应关系：

LST IMSIVLR:;

```
%%LST IMSIVLR:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 IMSI             VLR号   

 123030000000001  86139027
 123030000000002  86139028
(结果个数 = 2)

---    END
```

2.查询指定IMSI“123030000000001”的IMSI与MSC/VLR对应关系记录：

LST IMSIVLR: IMSI="123030000000001";

```
%%LST IMSIVLR: IMSI="123030000000001";%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  IMSI  =  123030000000001
 VLR号  =  86139027
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI与VLR对应关系(LST-IMSIVLR)_26145450.md`
