---
id: UNC@20.15.2@MMLCommand@LST IMEIGP
type: MMLCommand
name: LST IMEIGP（查询IMEI群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMEIGP
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
- 业务安全管理
- 用户终端管理
- IMEI群组管理
status: active
---

# LST IMEIGP（查询IMEI群组）

## 功能

**适用网元：SGSN、MME**

此命令用于查询IMEI群组记录。

## 注意事项

不输入任何参数，则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：可选参数<br>参数含义：待查询的IMEI群组标识。<br>取值范围：1~50<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMEIGP]] · IMEI群组（IMEIGP）

## 使用实例

查询所有IMEI群组记录：

LST IMEIGP:;

```
%%LST IMEIGP:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 IMEI群组标识    IMEI群组名称

 1              huawei         
 11             iphone         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMEIGP.md`
