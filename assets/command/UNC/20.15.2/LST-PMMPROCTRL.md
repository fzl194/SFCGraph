---
id: UNC@20.15.2@MMLCommand@LST PMMPROCTRL
type: MMLCommand
name: LST PMMPROCTRL（查询Iu模式移动性管理流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PMMPROCTRL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- Iu模式MM流程控制参数
status: active
---

# LST PMMPROCTRL（查询Iu模式移动性管理流程控制参数）

## 功能

**适用网元：SGSN**

此命令用于查询Iu模式移动性管理流程控制参数。

## 注意事项

- 此命令执行后立即生效。
- 若不输入流程类型，则将显示所有流程类型的原因值。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：待查询的流程类型。<br>取值范围：<br>- “ATTACH(附着流程)”<br>- “INTER_RAU(USN间路由区域更新流程)”<br>- “INTRA_RAU(USN内路由区域更新流程)”<br>- “UPDATE_LOCATION(位置更新流程)”<br>- “IU_RELEASE(Iu连接释放流程)”<br>- “AIR(获取鉴权集流程)”<br>- “AUTHENTICATION(鉴权流程)”<br>- “CHECK_IMEI(检查IMEI流程)”<br>- “PAGING(寻呼流程)”<br>- “CANCEL_LOCATION(位置取消流程)”<br>- “NET_SHARE(网络共享)”<br>默认值：无 |

## 操作的配置对象

- [Iu模式移动性管理流程控制参数（PMMPROCTRL）](configobject/UNC/20.15.2/PMMPROCTRL.md)

## 使用实例

查询流程类型为UPDATE_LOCATION（位置更新流程）的Iu模式移动性管理流程控制参数：

LST PMMPROCTRL: PROT=UPDATE_LOCATION;

```
%%LST PMMPROCTRL: PROT=UPDATE_LOCATION;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                    ULR拒绝原因值（IMSIGT错误）=  0
                    ULR拒绝原因值（SCCPGT错误）=  0
                      ULR拒绝原因值（链路异常）=  0
                   ULR拒绝原因值（HLR/HSS超时）=  0
                   ULR拒绝原因值（HLR/HSS拒绝）=  0
        ULR拒绝原因值（Diagnose为IMSI Unknown）=  0
ULR拒绝原因值（Diagnose为Subscription Unknown）=  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式移动性管理流程控制参数(LST-PMMPROCTRL)_72345115.md`
