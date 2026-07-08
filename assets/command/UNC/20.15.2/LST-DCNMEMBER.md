---
id: UNC@20.15.2@MMLCommand@LST DCNMEMBER
type: MMLCommand
name: LST DCNMEMBER（查询DCN成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DCNMEMBER
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN成员管理
status: active
---

# LST DCNMEMBER（查询DCN成员）

## 功能

**适用网元：MME**

该命令用于查询DCN下的MME组成员信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：可选参数<br>参数含义：该参数用来指定DCN标识。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置指定DCN的MME群组标识。<br>数据来源：全网规划<br>取值范围：4位16进制编码，范围为0000~FFFF。<br>默认值：无 |

## 操作的配置对象

- [DCN成员（DCNMEMBER）](configobject/UNC/20.15.2/DCNMEMBER.md)

## 使用实例

查询 “DCN ID” 为 “0” 的DCN下的MME成员：

LST DCNMEMBER: DCNID=0;

```
%%LST DCNMEMBER: DCNID=0;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
     DCN ID  =  0
MME组识别码  =  A1B3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DCN成员(LST-DCNMEMBER)_26145832.md`
