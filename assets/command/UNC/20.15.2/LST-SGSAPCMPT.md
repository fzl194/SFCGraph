---
id: UNC@20.15.2@MMLCommand@LST SGSAPCMPT
type: MMLCommand
name: LST SGSAPCMPT（查询SGsAP协议兼容性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSAPCMPT
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
- SGSAP
- SGsAP协议兼容性
status: active
---

# LST SGSAPCMPT（查询SGsAP协议兼容性）

## 功能

**适用网元：MME**

该命令用于查询SGsAP接口协议兼容性开关参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSAPCMPT]] · SGsAP协议兼容性（SGSAPCMPT）

## 使用实例

查询SGsAP协议兼容性：

LST SGSAPCMPT:;

```
%%LST SGSAPCMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                     TAI  =  按协议定义携带
                   E-CGI  =  按协议定义携带
TMSI based NRI container  =  不携带
             设置特殊LAI  =  否
                     LAI  =  NULL
          UE不可达原因值  =  UE不可达
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSAPCMPT.md`
