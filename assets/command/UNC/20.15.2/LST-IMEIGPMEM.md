---
id: UNC@20.15.2@MMLCommand@LST IMEIGPMEM
type: MMLCommand
name: LST IMEIGPMEM（查询IMEI群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMEIGPMEM
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
- IMEI群组成员管理
status: active
---

# LST IMEIGPMEM（查询IMEI群组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于查询IMEI群组成员。

## 注意事项

不输入任何参数，表示查询所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：可选参数<br>参数含义：待查询的IMEI群组标识。<br>取值范围：1~50<br>默认值：无 |
| IMEITAC | IMEI设备型号核准号码 | 可选必选说明：可选参数<br>参数含义：待查询用户的设备型号核准号码（TAC）。TAC由IMEI的前8位数字组成，由欧洲型号认证中心分配，用来标识某一型号的手机。<br>取值范围：8位十进制数<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMEIGPMEM]] · IMEI群组成员（IMEIGPMEM）

## 使用实例

查询IMEI群组标识为1的成员记录：

LST IMEIGPMEM: IMEIGPID=1;

```
%%LST IMEIGPMEM: IMEIGPID=1;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
 IMEI群组标识  IMEI设备型号核准号码   终端详细信息

 1             35437906               IPHONE
 1             86570702               HUAWEI
 (结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMEIGPMEM.md`
